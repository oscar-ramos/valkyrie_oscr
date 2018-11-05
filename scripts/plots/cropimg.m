
folder = '~/';
maxnum = 9;
for k=1:maxnum
    I = imread([folder num2str(k) '.png']);
    %imshow(I)
    Io = I(150:630, 490:960, :);
    outname = ['m4_out_' num2str(k) '.png']
    imwrite(Io, [folder outname])
    imshow(Io)
end
