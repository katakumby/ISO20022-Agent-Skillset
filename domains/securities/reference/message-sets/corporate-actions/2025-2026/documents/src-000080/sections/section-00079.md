---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.27 ElectionType <ElctnTp>"]
file_pages: [125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.27 ElectionType <ElctnTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 125 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 125

```text
Definition: Specifies whether the financial instrument calculates the taxable income per dividend/taxable
income per share.
TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> contains one of the following
elements (see "TaxableIncomePerShareCalculatedFormat3Choice" on page 965 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 965
Or}   Proprietary <Prtry> [1..1] ± 965
3.4.10.27  ElectionType <ElctnTp>
Presence: [0..1]
Definition: Specifies the effect on the holdings of electing a corporate action option.
ElectionType <ElctnTp> contains one of the following elements (see "ElectionTypeFormat3Choice" on
page 921 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 921
Or}   Proprietary <Prtry> [1..1] ± 921
3.4.10.28  LotteryType <LtryTp>
Presence: [0..1]
Definition: Specifies the type of lottery announced.
LotteryType <LtryTp> contains one of the following elements (see "LotteryTypeFormat4Choice" on
page 979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
3.4.10.29  CertificationType <CertfctnTp>
Presence: [0..1]
Definition: Specifies the certification format required, this is, physical or electronic format.
CertificationType <CertfctnTp> contains one of the following elements (see
"CertificationTypeFormat3Choice" on page 984 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 984
Or}   Proprietary <Prtry> [1..1] ± 984
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 125 February 2026
```

