import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MentorPage } from './mentor.page';

describe('MentorPage', () => {
  let component: MentorPage;
  let fixture: ComponentFixture<MentorPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MentorPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MentorPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
