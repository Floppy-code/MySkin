import { Component, EventEmitter, Output } from '@angular/core';
import { FormRecord } from '@angular/forms';
import { ImageCroppedEvent, LoadedImage } from 'ngx-image-cropper';
import { Observable } from 'rxjs';
import { PredictionEncodedFile } from 'src/app/core/model/prediction-encoded-file';
import { PredictionService } from '../../service/prediction.service';

@Component({
  selector: 'app-detection-upload',
  templateUrl: './detection-upload.component.html',
  styleUrls: ['./detection-upload.component.scss'],
})
export class DetectionUploadComponent {
  @Output() photoUploadedEvent = new EventEmitter<string>();

  imageChangedEvent: any = '';
  croppedImage?: any = '';

  fileChangeEvent(event: any): void {
    this.imageChangedEvent = event;
  }
  imageCropped(event: ImageCroppedEvent) {
    this.croppedImage = event.base64;
  }
  imageLoaded(image: LoadedImage) {
    // show cropper
  }
  cropperReady() {
    // cropper ready
  }
  loadImageFailed() {
    // show message
  }
  uploadPhoto() {
    console.log('Photo upload pressed!' + this.croppedImage);
    this.photoUploadedEvent.emit(this.croppedImage);
  }
}
