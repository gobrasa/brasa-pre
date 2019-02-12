import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { MenteeService } from './shared/mentee.service';
import { MenteeListComponent } from './components/mentee-list.component';
import { MenteeListingPage } from './mentee-listing/mentee-listing.page';
import { MenteeCollegePage } from './mentee-college/mentee-college.page';
import { MenteeDetailPage } from './mentee-detail/mentee-detail.page';
import { LoaderService } from '../shared/service/loader.service'
import { ToastService } from '../shared/service/toast.service';
import { AlertService } from '../shared/service/alert.service';
import { MenteeTestPage } from './mentee-test/mentee-test.page';
import { MenteeEssayPage } from './mentee-essay/mentee-essay.page';
import { IonicModule } from '@ionic/angular';
import { MenteePage } from './mentee/mentee.page';
import { MenteeInformationPage } from './mentee-information/mentee-information.page';
import { IonicSelectableModule } from 'ionic-selectable';
/*const routes: Routes = [
  {
    path: '',
    component: MenteePage,
    children: [
      {
        path: 'detail',
        component: MenteeDetailPage
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
    IonicSelectableModule,
    HttpClientModule
  ],
  providers: [
    MenteeService
  ],
  declarations: [
    MenteePage,
    MenteeDetailPage,
    MenteeListingPage,
    MenteeTestPage,
    MenteeCollegePage,
    MenteeEssayPage,
    MenteeListingPage,
    MenteeListComponent,
    MenteeInformationPage
  ]
})
export class MenteePageModule {}
