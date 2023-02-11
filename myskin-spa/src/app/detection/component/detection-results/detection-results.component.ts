import { Component, Input } from '@angular/core';
import { Observable } from 'rxjs';
import { PredictionResult } from 'src/app/core/model/prediction-result';

@Component({
  selector: 'app-detection-results',
  templateUrl: './detection-results.component.html',
  styleUrls: ['./detection-results.component.scss'],
})
export class DetectionResultsComponent {
  @Input() predictionResult$?: Observable<PredictionResult>;

  displayedColumns: string[] = ['Confidence', 'Type'];
  predictionResultTable?: PredictionResult[];

  constructor() {
    this.handlePredictionResult();
  }

  handlePredictionResult(): void {
    this.predictionResult$?.subscribe((predictionResult) => {
      console.log('Prediction results updated!');
      this.predictionResultTable = [predictionResult];
    });
  }
}
