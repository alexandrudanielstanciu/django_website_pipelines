from django.shortcuts import render
from imageloader.forms import *
from imageloader.sqlite3_helper import *
from imageloader.opencv_helper import *
from .models import *

import os,json

images = get_images()
pipelines = get_pipelines()
selected = []

def index(request):
    # Add data to database
    new = Image(0,'lion','images/lion.jpg')
    new.save()
    new = Image(1,'monitor','images/monitor.jpeg')
    new.save()
    new = Image(2,'stairs','images/stairs.jpg')
    new.save()
    new = Image(3,'lake','images/lake.jpg')
    new.save()

    new = Pipeline(0, '{"1":"Crop"}')
    new.save()
    new = Pipeline(1, '{"1":"Blur", "2":"Blur", "3":"Edge"}')
    new.save()
    new = Pipeline(2, '{"1":"Edge", "2":"Edge", "3":"Edge"}')
    new.save()
    new = Pipeline(3, '{"1":"Blur", "2":"Blur", "3":"Blur", "4":"MedianBlur"}')
    new.save()
    new = Pipeline(4, '{"1":"Blur", "2":"BilateralFiltering", "3":"GaussianBlur"}')
    new.save()


    img_paths = []
    for image in images:
        img_paths.append(image[2])

    if request.method == 'POST':
        image_selection = ImagesForm(request.POST)
        pipeline_selection = PipelinesForm(request.POST)

        if image_selection.is_valid() and pipeline_selection.is_valid():
            selected_images = image_selection.cleaned_data['SelectedImages']
            selected_pipelines = pipeline_selection.cleaned_data['SelectedPipelines']
            img_paths = []
            for choice in selected_images:
                key_to_search = int(choice)
                # Parse images and apply actions
                for image in images:
                    if (image[0] == key_to_search):
                        image_path = os.getcwd() + '/static/' + image[2]
                        # Parse each pipelines and write the result
                        for pipeline in pipelines:
                            pipeline_id = pipeline[0]
                            pipeline_chain = pipeline[1]
                            if str(pipeline_id) not in selected_pipelines:
                                continue
                            current = json.loads(str(pipeline_chain))
                            for key, value in current.items():
                                img = read_image(image_path)
                                if (value == 'Blur'):
                                    img = apply_blur(img)
                                elif (value == 'MedianBlur'):
                                    img = apply_median_blur(img)
                                elif (value == 'GaussianBlur'):
                                    img = apply_gaussian_blur(img)
                                elif (value == 'BilateralFiltering'):
                                    img = apply_bilateral_filtering(img)
                                elif (value == 'Edge'):
                                     img = apply_edge_cascade(img)
                                elif (value == 'Crop'):
                                    img = apply_crop(img)

                            new_path = os.getcwd() + '/static/' + "images/" + str(key_to_search) + "_" + str(pipeline[0]) + ".jpg"
                            short_path = "images/" + str(key_to_search) + "_" + str(pipeline[0]) + ".jpg"
                            img_paths.append(short_path)
                            write_image(new_path, img)
            context = {
                'paths': img_paths
            }

            return render(request, 'result.html', context=context)
    else:
        image_selection = ImagesForm()
        pipeline_selection = PipelinesForm()


    context = {'image_selection': image_selection,
               'pipeline_selection': pipeline_selection,
               'paths': img_paths}
    return render(request, 'index.html', context = context)
