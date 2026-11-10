---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.11 DateDetails <DtDtls>", "8.4.12.11.11.5 PaymentDate <PmtDt>"]
file_pages: [649]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.11.5 PaymentDate <PmtDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 649 to 649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 649

```text
Definition: Date/time on which a payment can be made, for example, if the payment date is a non-
business day or to indicate the first payment date of an offer.
Datatype: "ISODate" on page 1243
8.4.12.11.11.5  PaymentDate <PmtDt>
Presence: [0..1]
Definition: Date on which the distribution is due to take place (cash and/or securities).
Datatype: "ISODate" on page 1243
8.4.12.11.12  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Exchange rate between the amount and the resulting amount.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms40"
on page 1023 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 1023
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 1023
   ExchangeRate <XchgRate> [1..1] Rate 1024
   ResultingAmount <RsltgAmt> [1..1] Amount C1, C10 1024
8.4.12.11.13  TaxDocumentationDetails <TaxDcmnttnDtls>
Presence: [0..1]
Definition: Provides information about the tax voucher related to a cash movement.
Impacted by: C9 "BeneficialOwnerReferencePresenceRule", C71
"TaxReclaimDocumentationReferencePresenceRule", C72 "TaxVoucherPresenceRule"
TaxDocumentationDetails <TaxDcmnttnDtls> contains the following elements (see "TaxVoucher6"
on page 985 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxVoucherReference <TaxVchrRef> [0..1] Text 985
   TaxReclaimDocumentationReference
<TaxRclmDcmnttnRef>
[0..1] Text 985
   BeneficialOwnerReference <BnfclOwnrRef> [0..1] Text 985
Constraints
• BeneficialOwnerReferencePresenceRule
If BeneficialOwnerReference is present then TaxReclaimDocumentationReference must be absent.
On Condition
    /BeneficialOwnerReference is present
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 649 February 2026
```

