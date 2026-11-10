---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.2 TypeOfRequest <TpOfReq>", "32.4.2.2.1 Code <Cd>"]
file_pages: [792]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 792 to 792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 792

```text
TypeOfRequest <TpOfReq> contains one of the following TypeOfRequest1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 792
Or}   Proprietary <Prtry> [1..1] ± 792
32.4.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of request expressed as a code.
Datatype: "TypeOfRequest1Code" on page 5387
CodeName Name Definition
INFO Information Request for information.
STAT Status Request for status.
32.4.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of request expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
32.4.2.3  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
32.4.2.4  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identification of the transfer, as assigned by the instructing party.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 792 May 2026
```

