import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DetectionBaseComponent } from './component/detection-base/detection-base.component';
import { DetectionUploadComponent } from './component/detection-upload/detection-upload.component';
import { DetectionResultsComponent } from './component/detection-results/detection-results.component';
import { DetectionHistoryComponent } from './component/detection-history/detection-history.component';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatTableModule } from '@angular/material/table';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatIconModule } from '@angular/material/icon';
import { RouterModule } from '@angular/router';
import { NgxDropzoneModule } from 'ngx-dropzone';
import { ImageCropperModule } from 'ngx-image-cropper';

@NgModule({
  declarations: [
    DetectionBaseComponent,
    DetectionUploadComponent,
    DetectionResultsComponent,
    DetectionHistoryComponent,
  ],
  imports: [
    CommonModule,
    ImageCropperModule,
    MatCardModule,
    MatIconModule,
    MatButtonModule,
    MatDividerModule,
    MatExpansionModule,
    RouterModule,
    NgxDropzoneModule,
    MatTableModule,
  ],
})
export class DetectionModule {}
