---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.3 Pension <Pnsn>", "36.4.15.5.3.3 TransferScope <TrfScp>"]
file_pages: [1174]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.3.3 TransferScope <TrfScp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1174 to 1174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1174

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
36.4.15.5.3.3  TransferScope <TrfScp>
Presence: [0..1]
Definition: Scope of the pension policy, plan or scheme transfer.
TransferScope <TrfScp> contains one of the following elements (see "PensionTransferScope1Choice"
on page 4710 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4711
Or}   Proprietary <Prtry> [1..1] ± 4711
36.4.15.5.3.4  TaxReference <TaxRef>
Presence: [0..*]
Definition: Tax reference issued to the pension policy, plan or scheme by a central organisation.
TaxReference <TaxRef> contains the following elements (see "TaxReference1" on page 5234 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxType <TaxTp> [0..1]  5235
{Or     Code <Cd> [1..1] CodeSet 5235
Or}     Proprietary <Prtry> [1..1] ± 5235
   Reference <Ref> [1..1] Text 5236
   HolderType <HldrTp> [0..1]  5236
{Or     Code <Cd> [1..1] CodeSet 5236
Or}     Proprietary <Prtry> [1..1] ± 5236
36.4.15.5.3.5  DrawdownTrancheIdentification <DrwdwnTrchId>
Presence: [0..1]
Definition: Reference of the drawdown.
Datatype: "Max35Text" on page 5403
36.4.15.5.3.6  DrawdownStatus <DrwdwnSts>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1174 May 2026
```

