---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.62 TaxVoucher6"]
file_pages: [985]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.62 TaxVoucher6

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 985 to 985.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 985

```text
16.1.15.62  TaxVoucher6
Definition: Specifies tax vouchers in the framework of a corporate action event.
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
Following Must be True
    /TaxReclaimDocumentationReference Must be absent
• TaxReclaimDocumentationReferencePresenceRule
If TaxReclaimDocumentationReference is present then BeneficialOwnerReference must be absent.
On Condition
    /TaxReclaimDocumentationReference is present
Following Must be True
    /BeneficialOwnerReference Must be absent
• TaxVoucherPresenceRule
At least one of TaxVoucherReference Or TaxReclaimDocumentationReference Or
BeneficialOwnerReference must be present.
Following Must be True
    /TaxVoucherReference Must be present
 Or    /TaxReclaimDocumentationReference Must be present
 Or    /BeneficialOwnerReference Must be present
16.1.15.62.1  TaxVoucherReference <TaxVchrRef>
Presence: [0..1]
Definition: Unique reference for the tax voucher required by the relevant tax authorities to ensure that
any claim relating to this particular tax voucher cannot be duplicated.
Datatype: "Max35Text" on page 1251
16.1.15.62.2  TaxReclaimDocumentationReference <TaxRclmDcmnttnRef>
Presence: [0..1]
Definition: Unique reference assigned by the account owner to the tax documentation sent to the
account servicer for processing.
Datatype: "Max35Text" on page 1251
16.1.15.62.3  BeneficialOwnerReference <BnfclOwnrRef>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 985 February 2026
```

