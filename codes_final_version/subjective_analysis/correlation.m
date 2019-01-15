results = zeros(4, 4);
PSNR = {};

%get the objective scores computed by the IQA metric and the subjective
%scores provided by the dataset
Obj_jiayu = load('jiayu_psnr.mat');
Obj_sitzmann = load('sitzmann_psnr.mat');
SubData = load('S_MOS.mat');

% PSNR(1)--psnr, PSNR(2)--ws_psnr, PSNR(3)--va_psnr(sitzmann), PSNR(4)--va_psnr(jiayu)
PSNR{1} = reshape(Obj_jiayu.psnr, [], 1);
PSNR{2} = reshape(Obj_jiayu.ws_psnr, [], 1);
PSNR{3} = reshape(Obj_sitzmann.va_psnr, [], 1);
PSNR{4} = reshape(Obj_jiayu.va_psnr, [], 1);
MOS = reshape(SubData.S_MOS, [], 1);

figure(4);
figure('Renderer', 'painters', 'Position', [10 10 900 600])
% set(gcf,'unit','centimeters','position',[10 10 41 10]);
temp = {'PSNR', 'WS-PSNR', 'VA-PSNR(Sitzmann)', 'VA-PSNR(Jiayu)'};
name = string(temp);

for i = 1:4
    %initialize the parameters used by the nonlinear fitting function
    beta(1) = max(MOS);
    beta(2) = min(MOS);
    beta(3) = mean(PSNR{i});
    beta(4) = 0.1;
    beta(5) = 0.1;
    
    opts = statset('nlinfit');
    opts.RobustWgtFun = 'bisquare';

    %fitting a curve using the data
    [bayta ehat,J] = nlinfit(PSNR{i}, MOS,@logistic,beta);
    %given a ssim value, predict the correspoing mos (ypre) using the fitted curve
    [ypre junk] = nlpredci(@logistic,PSNR{i},bayta,ehat,J);

    results(i,1) = sqrt(sum((ypre - MOS).^2) / length(MOS)); %rmse
    results(i,2) = corr(MOS, ypre, 'type','Pearson'); %plcc
    results(i,3) = corr(MOS, ypre, 'type','spearman'); %srocc
    results(i,4) = corr(MOS, ypre, 'type','Kendall'); %krocc
    
    subplot(2, 2, i);
    % plot(PSNR{i},MOS,'+');
    set(plot(PSNR{i},MOS,'+'),'Color','yellow','LineWidth',1);
    t = min(PSNR{i}):0.01:max(PSNR{i});
    [ypre junk] = nlpredci(@logistic,t,bayta,ehat,J);
    hold on;
    
    c = polyfit(t, ypre, 2);
    d = polyval(c, t, 1);

    set(plot(t, d, 'r'),'Color','k','LineWidth',2);
    legend('Images','Curve fitted', 'Location','SouthEast');
    xlabel('Objective score by ' + name(1, i));
    ylabel('MOS');
end 
disp(results)

save('corr_jiayu.mat', 'results');
saveas(gcf, 'corr_jiayu.png');



Objective_Metrics = ["PSNR"; "WS-PSNR"; "VA-PSNR(Sitzmann)"; "VA-PSNR(Jiayu)"];
RMSE = results(:, 1);
PLCC = results(:, 2);
SROCC = results(:, 3);
KROCC = results(:, 4);

T = table(Objective_Metrics,RMSE,PLCC,SROCC,KROCC)