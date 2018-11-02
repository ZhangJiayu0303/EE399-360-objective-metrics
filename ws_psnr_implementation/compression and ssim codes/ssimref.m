I = imread('/Users/zhangjiayu/Desktop/bedroom.jpg');

ssimValues = zeros(1,10);
qualityFactor = 25:25:100;
for i = 1:4
    filename = ['/Users/zhangjiayu/Desktop/compressed pictures/compressedBedroom', num2str(i * 25), '.jpg'];
    ssimValues(i) = ssim(imread(filename),I);
end

plot(qualityFactor,ssimValues,'b-o');

xlabel('Compression Quality Factor');
ylabel('SSIM Value');