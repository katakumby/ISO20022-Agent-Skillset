---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.10 PostingQuantity <PstngQty>"]
file_pages: [600]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.10 PostingQuantity <PstngQty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 600 to 600.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 600

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
8.4.12.10.10  PostingQuantity <PstngQty>
Presence: [1..1]
Definition: Quantity of securities that have been posted (credit or debit) to the safekeeping account.
PostingQuantity <PstngQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
8.4.12.10.11  SafekeepingPlace <SfkpgPlc>
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
8.4.12.10.12  FractionDisposition <FrctnDspstn>
Presence: [0..1]
Definition: Specifies how fractions resulting from derived securities will be processed or how prorated
decisions will be rounding, if provided with a pro ration rate.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 600 February 2026
```

