---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.10 MovementDetails <MvmntDtls>", "74.4.3.4.10.1 BalanceFrom <BalFr>"]
file_pages: [2631]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.10.1 BalanceFrom <BalFr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2631 to 2631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2631

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageOriginator <MsgOrgtr> [0..1] ± 2641
   CreationDateTime <CreDtTm> [1..1] DateTime 2641
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 2641
   SupplementaryData <SplmtryData> [0..*] ± C24 2641
74.4.3.4.10.1  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the securities are moving.
BalanceFrom <BalFr> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 2854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 2854
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2854
74.4.3.4.10.2  BalanceTo <BalTo>
Presence: [1..1]
Definition: Balance to which the securities are moving.
BalanceTo <BalTo> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 2854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 2854
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2854
74.4.3.4.10.3  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C9 "DescriptionPresenceRule", C10 "DescriptionUsageRule", C12 "ISINGuideline", C13
"ISINPresenceRule", C15 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2631 August 2026
```

