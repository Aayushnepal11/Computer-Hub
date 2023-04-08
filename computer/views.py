from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, View, UpdateView, FormView
from .models import ComputerBarnd, ComputerSpecification, Computer
from .forms import EditForm, CreateData
from django.contrib import messages

class HomePageView(ListView):
    template_name = "index.html"
    model = ComputerBarnd
    context_object_name = "computer_brand"

    
class ProuctSpecification(View):
    def get(self, request, pk):
        # data = ComputerBarnd.objects.get(id=pk)
        data = get_object_or_404(ComputerBarnd, id=pk)
        fetch_spec = data.brands.all()
        context = {
            "title": "Product Spec Details",
            "data": data,
            "spec_data": fetch_spec
        }
        
        return render(request, "product_spec.html", context)

class ViewOrderPage(View):
    def get(self, request, id):
        # data_set = ComputerSpecification.objects.get(id=id)
        data_set = get_object_or_404(ComputerSpecification, id=id)
        new_data = data_set.computer.all()

        context = {
            'title': 'Product Page',
            "data_set": data_set,
            "fetch_data": new_data,
        }

        return render(request, "view_order.html", context)

class OrderUpdateView(UpdateView):
    model = Computer
    template_name = "update_order.html"
    form_class = EditForm

    def form_valid(self, form):
        messages.success(self.request, "Data is valid.")
        form.instance.user = self.request.user
        form.save()
        return redirect("computer_hub:home")
    
    def get_success_url(self):
        messages.success(self.request, "Data update successfully.")
        return redirect("computer_hub:home")
    
    
class DataCreateView(FormView):
    model = ComputerSpecification
    template_name = "create_spec.html"
    form_class = CreateData
    success_url = "Your data has been saved."

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Data has been Added.")
        return redirect("computer_hub:home")

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)