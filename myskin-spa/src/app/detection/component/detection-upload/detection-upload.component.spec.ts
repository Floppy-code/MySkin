import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetectionUploadComponent } from './detection-upload.component';

describe('DetectionUploadComponent', () => {
  let component: DetectionUploadComponent;
  let fixture: ComponentFixture<DetectionUploadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetectionUploadComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetectionUploadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
