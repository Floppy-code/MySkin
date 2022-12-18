import { Component } from '@angular/core';
import { FormRecord } from '@angular/forms';
import { Observable } from 'rxjs';
import { PredictionEncodedFile } from 'src/app/core/model/prediction-encoded-file';
import { PredictionService } from '../../service/prediction.service';

@Component({
  selector: 'app-detection-upload',
  templateUrl: './detection-upload.component.html',
  styleUrls: ['./detection-upload.component.scss'],
})
export class DetectionUploadComponent {
  files: File[] = [];

  constructor(private predictionService: PredictionService) {}

  onSelect(event: any): void {
    console.log(event);
    this.files.push(...event.addedFiles);
  }

  onRemove(event: any) {
    console.log(event);
    this.files.splice(this.files.indexOf(event), 1);
  }

  uploadPhoto(): void {
    console.log('Uploading photo!');
    this.predictionService.predict(this.files[0]);
  }
}
