---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.5 CorporateActionInstruction <CorpActnInstr>", "13.4.5.11 InstructedBalance <InstdBal>"]
file_pages: [752]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.5.11 InstructedBalance <InstdBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 752 to 752.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 752

```text
13.4.5.11  InstructedBalance <InstdBal>
Presence: [0..1]
Definition: Balance of instructed position.
InstructedBalance <InstdBal> contains the following elements (see "SignedQuantityFormat11" on
page 1094 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1094
   QuantityChoice <QtyChc> [1..1]  1094
{Or     Quantity <Qty> [1..1] ± C13 1095
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1095
       Quantity <Qty> [1..1] Quantity 1095
       QuantityType <QtyTp> [1..1] Text 1095
       Issuer <Issr> [1..1] Text 1095
       SchemeName <SchmeNm> [0..1] Text 1096
13.4.5.12  UninstructedBalance <UinstdBal>
Presence: [0..1]
Definition: Balance of uninstructed position.
UninstructedBalance <UinstdBal> contains the following elements (see "SignedQuantityFormat11"
on page 1094 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1094
   QuantityChoice <QtyChc> [1..1]  1094
{Or     Quantity <Qty> [1..1] ± C13 1095
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1095
       Quantity <Qty> [1..1] Quantity 1095
       QuantityType <QtyTp> [1..1] Text 1095
       Issuer <Issr> [1..1] Text 1095
       SchemeName <SchmeNm> [0..1] Text 1096
13.4.5.13  ProtectBalance <PrtctBal>
Presence: [0..1]
Definition: Balance of securities which are in protect status in a CSD operating a protect cover service.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 752 February 2026
```

