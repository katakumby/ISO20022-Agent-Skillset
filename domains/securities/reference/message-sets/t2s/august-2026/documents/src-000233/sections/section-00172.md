---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.4 Message Building Blocks", "13.4.7 CashAccountServicer <CshAcctSvcr>"]
file_pages: [224, 225]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.4.7 CashAccountServicer <CshAcctSvcr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 224 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
Definition: Party that legally owns the cash account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
13.4.7 CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
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
13.4.8 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Impacted by: C3 "AdditionalDetailsRule", C6 "BalanceFromToRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 224 August 2026
```

## File page 225

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 226
   SettlementDate <SttlmDt> [1..1] ± 226
   BalanceFrom <BalFr> [1..1]  226
     Type <Tp> [1..1]  226
{Or       Code <Cd> [1..1] CodeSet 227
Or}       Proprietary <Prtry> [1..1] ± 227
     QuantityBreakdown <QtyBrkdwn> [0..*]  227
       LotNumber <LotNb> [0..1] ± 227
       LotAmount <LotAmt> [0..1] ± 228
       LotQuantity <LotQty> [0..1] ± 228
       CashSubBalanceType <CshSubBalTp> [0..1] ± 228
   BalanceTo <BalTo> [1..1]  229
     Type <Tp> [1..1]  229
{Or       Code <Cd> [1..1] CodeSet 229
Or}       Proprietary <Prtry> [1..1] ± 229
     QuantityBreakdown <QtyBrkdwn> [0..*]  230
       LotNumber <LotNb> [0..1] ± 230
       LotAmount <LotAmt> [0..1] ± 230
       LotQuantity <LotQty> [0..1] ± 231
       CashSubBalanceType <CshSubBalTp> [0..1] ± 231
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 231
   Priority <Prty> [0..1] ± 231
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 232
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
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 225 August 2026
```

