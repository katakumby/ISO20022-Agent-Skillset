---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "8.4 Message Building Blocks", "8.4.7 CashAccountServicer <CshAcctSvcr>"]
file_pages: [141, 142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 8.4.7 CashAccountServicer <CshAcctSvcr>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 141 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
Definition: Party that legally owns the cash account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 420
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 420
8.4.7 CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
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
8.4.8 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Impacted by: C3 "AdditionalDetailsRule", C6 "BalanceFromToRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
141 March 2024
```

## File page 142

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 143
   SettlementDate <SttlmDt> [1..1] ± 143
   BalanceFrom <BalFr> [1..1]  143
     Type <Tp> [1..1]  143
{Or       Code <Cd> [1..1] CodeSet 144
Or}       Proprietary <Prtry> [1..1] ± 144
     QuantityBreakdown <QtyBrkdwn> [0..*]  144
       LotNumber <LotNb> [0..1] ± 144
       LotAmount <LotAmt> [0..1] ± 145
       LotQuantity <LotQty> [0..1] ± 145
       CashSubBalanceType <CshSubBalTp> [0..1] ± 145
   BalanceTo <BalTo> [1..1]  146
     Type <Tp> [1..1]  146
{Or       Code <Cd> [1..1] CodeSet 146
Or}       Proprietary <Prtry> [1..1] ± 146
     QuantityBreakdown <QtyBrkdwn> [0..*]  147
       LotNumber <LotNb> [0..1] ± 147
       LotAmount <LotAmt> [0..1] ± 147
       LotQuantity <LotQty> [0..1] ± 148
       CashSubBalanceType <CshSubBalTp> [0..1] ± 148
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 148
   Priority <Prty> [0..1] ± 148
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 149
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can be
provided in a structured field.
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
142 March 2024
```

