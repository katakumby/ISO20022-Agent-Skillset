---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.11 SafekeepingPlace <SfkpgPlc>"]
file_pages: [187]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.11 SafekeepingPlace <SfkpgPlc>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 187 to 187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 187

```text
EntitledQuantity <EntitldQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
3.4.11.24.11  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Location where the financial instruments are/will be safekept.
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat41Choice" on page 995 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  996
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 996
     Identification <Id> [0..1] Text 996
Or   Country <Ctry> [1..1] CodeSet C3 996
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 997
Or   TypeAndIdentification <TpAndId> [1..1]  997
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 997
     Identification <Id> [1..1] IdentifierSet C1 997
Or}   Proprietary <Prtry> [1..1] ± 998
3.4.11.24.12  CountryOfIncomeSource <CtryOfIncmSrc>
Presence: [0..1]
Definition: Indicates the country from which the income originates.
Impacted by: C17 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.4.11.24.13  FractionDisposition <FrctnDspstn>
Presence: [0..1]
Definition: Specifies how fractions resulting from derived securities will be processed or how prorated
decisions will be rounding, if provided with a pro ration rate.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 187 February 2026
```

