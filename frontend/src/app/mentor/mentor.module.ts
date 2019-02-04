import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { MentorService } from './shared/mentor.service';
import { MentorListComponent } from './components/mentor-list.component';
import { MentorListingPage } from './mentor-listing/mentor-listing.page';
import { MentorDetailPage } from './mentor-detail/mentor-detail.page';
import { LoaderService } from '../shared/service/loader.service'
import { ToastService } from '../shared/service/toast.service';
import { AlertService } from '../shared/service/alert.service';



import { IonicModule } from '@ionic/angular';
import { MentorPage } from './mentor/mentor.page';
import { MentorInformationPage } from './mentor-information/mentor-information.page';


/*const routes: Routes = [
  {
    path: '',
    component: MentorPage,
    children: [
      {
        path: 'detail',
        component: MentorDetailPage
      }
    ]
  }
];*/

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    IonicModule,
    HttpClientModule
  ],
  providers: [
    MentorService
  ],
  declarations: [
    MentorPage, 
    MentorDetailPage, 
    MentorListingPage, 
    MentorListingPage,
    MentorListComponent,
    MentorInformationPage,
    MentorInformationPage,

  ]
})
export class MentorPageModule {}