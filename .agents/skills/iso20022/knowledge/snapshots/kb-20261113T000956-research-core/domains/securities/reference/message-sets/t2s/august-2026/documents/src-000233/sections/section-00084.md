---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "8.4 Message Building Blocks", "8.4.8 UnderlyingIntraBalance <UndrlygIntraBal>"]
file_pages: [124, 125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 8.4.8 UnderlyingIntraBalance <UndrlygIntraBal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 124 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 2919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  2920
     BICFI <BICFI> [0..1] IdentifierSet C3 2920
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
     LEI <LEI> [0..1] IdentifierSet 2920
     Name <Nm> [0..1] Text 2921
     PostalAddress <PstlAdr> [0..1] ± 2921
     Other <Othr> [0..1] ± 2921
   BranchIdentification <BrnchId> [0..1]  2922
     Identification <Id> [0..1] Text 2922
     LEI <LEI> [0..1] IdentifierSet 2922
     Name <Nm> [0..1] Text 2922
     PostalAddress <PstlAdr> [0..1] ± 2923
8.4.8 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Impacted by: C3 "AdditionalDetailsRule", C6 "BalanceFromToRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 124 August 2026
```

## File page 125

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 126
   SettlementDate <SttlmDt> [1..1] ± 126
   BalanceFrom <BalFr> [1..1]  126
     Type <Tp> [1..1]  126
{Or       Code <Cd> [1..1] CodeSet 127
Or}       Proprietary <Prtry> [1..1] ± 127
     QuantityBreakdown <QtyBrkdwn> [0..*]  127
       LotNumber <LotNb> [0..1] ± 127
       LotAmount <LotAmt> [0..1] ± 128
       LotQuantity <LotQty> [0..1] ± 128
       CashSubBalanceType <CshSubBalTp> [0..1] ± 128
   BalanceTo <BalTo> [1..1]  129
     Type <Tp> [1..1]  129
{Or       Code <Cd> [1..1] CodeSet 129
Or}       Proprietary <Prtry> [1..1] ± 129
     QuantityBreakdown <QtyBrkdwn> [0..*]  130
       LotNumber <LotNb> [0..1] ± 130
       LotAmount <LotAmt> [0..1] ± 130
       LotQuantity <LotQty> [0..1] ± 131
       CashSubBalanceType <CshSubBalTp> [0..1] ± 131
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 131
   Priority <Prty> [0..1] ± 131
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 132
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 125 August 2026
```

