---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "3.4 Message Building Blocks", "3.4.8 UnderlyingIntraBalance <UndrlygIntraBal>"]
file_pages: [41, 42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 3.4.8 UnderlyingIntraBalance <UndrlygIntraBal>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 41 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  401
     BICFI <BICFI> [0..1] IdentifierSet C6 401
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 402
     LEI <LEI> [0..1] IdentifierSet 402
     Name <Nm> [0..1] Text 402
     PostalAddress <PstlAdr> [0..1] ± 402
     Other <Othr> [0..1] ± 403
   BranchIdentification <BrnchId> [0..1]  404
     Identification <Id> [0..1] Text 404
     LEI <LEI> [0..1] IdentifierSet 404
     Name <Nm> [0..1] Text 404
     PostalAddress <PstlAdr> [0..1] ± 404
3.4.8 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Impacted by: C3 "AdditionalDetailsRule", C6 "BalanceFromToRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
41 March 2024
```

## File page 42

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 43
   SettlementDate <SttlmDt> [1..1] ± 43
   BalanceFrom <BalFr> [1..1]  43
     Type <Tp> [1..1]  43
{Or       Code <Cd> [1..1] CodeSet 44
Or}       Proprietary <Prtry> [1..1] ± 44
     QuantityBreakdown <QtyBrkdwn> [0..*]  44
       LotNumber <LotNb> [0..1] ± 44
       LotAmount <LotAmt> [0..1] ± 45
       LotQuantity <LotQty> [0..1] ± 45
       CashSubBalanceType <CshSubBalTp> [0..1] ± 45
   BalanceTo <BalTo> [1..1]  46
     Type <Tp> [1..1]  46
{Or       Code <Cd> [1..1] CodeSet 46
Or}       Proprietary <Prtry> [1..1] ± 46
     QuantityBreakdown <QtyBrkdwn> [0..*]  47
       LotNumber <LotNb> [0..1] ± 47
       LotAmount <LotAmt> [0..1] ± 47
       LotQuantity <LotQty> [0..1] ± 48
       CashSubBalanceType <CshSubBalTp> [0..1] ± 48
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 48
   Priority <Prty> [0..1] ± 48
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 49
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
42 March 2024
```

