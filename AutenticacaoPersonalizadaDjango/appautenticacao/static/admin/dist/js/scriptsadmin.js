
$('#modal_excluir_registro').on('show.bs.modal', function (e) {
  $message = $(e.relatedTarget).attr('data-message');
  $(this).find('.modal-body p').text($message);
  $title = $(e.relatedTarget).attr('data-title');
  $(this).find('.modal-title').text($title);
  $id = $(e.relatedTarget).attr('data-id');
  $(this).find('.modal-id').text($id);
  $page = $(e.relatedTarget).attr('data-page');
  $(this).find('.modal-footer #confirm').text($title);
  $(this).find('.modal-page').text($page);
  // Pass form reference to modal for submission on yes/ok
  var form = $(e.relatedTarget).closest('form');
  $(this).find('.modal-footer #confirm').data('form', form);
});

$('#modal_excluir_registro').find('.modal-footer #confirm').on('click', function () {
     window.location=$page;
});
const checkboxtodos = document.querySelector("#selecionartodosck");
//const checkboxList = document.querySelectorAll("input[type='checkbox'][name='dadosexcluir']");
const checkboxList = document.querySelectorAll("input[type='checkbox']");
checkboxtodos.addEventListener("change", (event) => {
  const checkedAll = event.target.checked;
  checkboxList.forEach((checkbox) => {
    checkbox.checked = checkedAll;
  });
  checkboxList.forEach((checkbox) => {
    checkbox.setAttribute("data-check-all", checkedAll);
  });
});

$(function () {
    $.validator.setDefaults({
      submitHandler: function () {
        alert( "Form successful submitted!" );
      }
    });
    $('#form_cadusuarioAPOIS').validate({
      rules: {
        email: {
          required: true,
          email: true,
        },
        password: {
          required: true,
          minlength: 5
        },
        terms: {
          required: true
        },
      },
      messages: {
        email: {
          required: "Please enter a email address",
          email: "Please enter a valid email address"
        },
        password: {
          required: "Please provide a password",
          minlength: "Your password must be at least 5 characters long"
        },
        terms: "Please accept our terms"
      },
      errorElement: 'span',
      errorPlacement: function (error, element) {
        error.addClass('invalid-feedback');
        element.closest('.form-group').append(error);
      },
      highlight: function (element, errorClass, validClass) {
        $(element).addClass('is-invalid');
      },
      unhighlight: function (element, errorClass, validClass) {
        $(element).removeClass('is-invalid');
      }
    });
  });