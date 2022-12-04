import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetectionBaseComponent } from './detection-base.component';

describe('DetectionBaseComponent', () => {
  let component: DetectionBaseComponent;
  let fixture: ComponentFixture<DetectionBaseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetectionBaseComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetectionBaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
