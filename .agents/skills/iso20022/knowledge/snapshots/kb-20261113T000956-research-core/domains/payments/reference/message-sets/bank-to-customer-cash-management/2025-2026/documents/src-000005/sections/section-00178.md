---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.3 Transaction <Tx>", "2.4.2.15.18.2.26.3.2 Individual <Indv>", "2.4.2.15.18.2.26.3.2.3 AdditionalService <AddtlSvc>"]
file_pages: [256]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.3.2.3 AdditionalService <AddtlSvc>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 256 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
Definition: Entity or object in charge of verifying the cardholder authenticity.
Datatype: "AuthenticationEntity1Code" on page 888
CodeName Name Definition
ICCD ICC Application in the chip card (Integrated
Circuit Card), for instance an offline PIN
verification.
AGNT AuthorisedAgent Authorisation agent of the issuer.
MERC Merchant Merchant (for example signature
verification by the attendant).
2.4.2.15.18.2.26.3.2.3  AdditionalService <AddtlSvc>
Presence: [0..1]
Definition: Service in addition to the main service.
Datatype: "CardPaymentServiceType2Code" on page 890
CodeName Name Definition
AGGR Aggregation Aggregation of low payments.
DCCV DCC Dynamic currency conversion (DCC).
GRTT Gratuity Card payment with gratuity.
INSP Instalment Instalment payment.
LOYT Loyalty Loyalty services.
NRES NoShow No show after reservation.
PUCO PurchaseCorporate Purchase and corporate data.
RECP RecurringPayment Recurring payment.
SOAF SolicitedAvailableFunds Solicited available funds.
UNAF UnsolicitedAvailableFunds Unsolicited available funds.
VCAU VoiceAuthorisation Voice authorisation.
2.4.2.15.18.2.26.3.2.4  TransactionCategory <TxCtgy>
Presence: [0..1]
Definition: Category code conform to ISO 18245, related to the type of services or goods the merchant
provides for the transaction.
This element is also known as the MerchantCategoryCode.
Datatype: "ExternalCardTransactionCategory1Code" on page 894
2.4.2.15.18.2.26.3.2.5  SaleReconciliationIdentification <SaleRcncltnId>
Presence: [0..1]
Definition: Unique identification of the sales reconciliation period between the acceptor and the acquirer.
This identification might be linked to the identification of the settlement for further verification by the
merchant.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
256 March 2026
```

