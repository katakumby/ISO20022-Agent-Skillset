---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.10 MovementDetails <MvmntDtls>", "3.4.3.4.10.1 BalanceFrom <BalFr>"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.10.1 BalanceFrom <BalFr>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageOriginator <MsgOrgtr> [0..1] ± 86
   CreationDateTime <CreDtTm> [1..1] DateTime 86
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 86
   SupplementaryData <SplmtryData> [0..*] ± C24 86
3.4.3.4.10.1  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the securities are moving.
BalanceFrom <BalFr> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 199 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
3.4.3.4.10.2  BalanceTo <BalTo>
Presence: [1..1]
Definition: Balance to which the securities are moving.
BalanceTo <BalTo> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 199 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
3.4.3.4.10.3  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C9 "DescriptionPresenceRule", C10 "DescriptionUsageRule", C12 "ISINGuideline", C13
"ISINPresenceRule", C15 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 76 September 2025
```

