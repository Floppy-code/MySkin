import { Component, Input } from '@angular/core';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { PredictionHistoryService } from '../../service/prediction-history.service';

@Component({
  selector: 'app-detection-results',
  templateUrl: './detection-results.component.html',
  styleUrls: ['./detection-results.component.scss'],
})
export class DetectionResultsComponent {
  @Input() PredictionResult?: PredictionResult;

  displayedColumns: string[] = ['label-id', 'label-name', 'label-probability'];

  constructor() {}
}
