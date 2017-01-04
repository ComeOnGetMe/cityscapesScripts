from __future__ import print_function
import os, glob, sys, json

# Configurations
cityscapesPath = '/home/zhipeng_yan/Desktop/adas-segmentation-cityscape/data/cityscapes'
imgsize = (1024,2048)

def main():
    searchImg = os.path.join(cityscapesPath, 'leftImg8bit', '*', '*', '*_leftImg8bit.png')
    images = glob.glob(searchImg)
    images.sort()

    if not images:
        print('Did not find any images. Please check the directory')
        exit(1)

    fineDir = os.path.join(cityscapesPath, 'gtFine')
    if not os.path.isdir(fineDir):
        os.mkdir(fineDir)

    coarseDir = os.path.join(cityscapesPath, 'gtCoarse')
    if not os.path.isdir(coarseDir):
        os.mkdir(coarseDir)

    labelDir = {'Fine': fineDir, 'Coarse': coarseDir}

    print('Processing {} json files'.format(len(images)))

    progress = 0
    initial_json = {'imgHeight':imgsize[0], 'imgWidth':imgsize[1], 'objects': []}
    print('Progress: {:>3} %'.format( progress * 100/len(images) ), end=' ')
    for img in images:
        dataset, city, imgId = img.split('/')[-3:]
        for labelType, typeDir in labelDir.items():
            datasetDir = os.path.join(typeDir, dataset)
            if not os.path.isdir(datasetDir):
                os.mkdir(datasetDir)

            cityDir = os.path.join(datasetDir, city)
            if not os.path.isdir(cityDir):
                os.mkdir(cityDir)

            dst = os.path.join(cityDir, imgId.replace('leftImg8bit.png', 'gt'+labelType+'_polygons.json'))
            if not os.path.isfile(dst):
                with open(dst, 'w') as f:
                    json.dump(initial_json, f)

            # status
            progress += 1
            print('\rProgress: {:>3} %'.format( progress * 50/len(images) ), end=' ')
            sys.stdout.flush()

# call the main
if __name__ == "__main__":
    main()
