---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "12.4 Message Building Blocks", "12.4.5 CashAccountServicer <CshAcctSvcr>"]
file_pages: [206, 207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 12.4.5 CashAccountServicer <CshAcctSvcr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 206 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
12.4.5 CashAccountServicer <CshAcctSvcr>
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
12.4.6 UnderlyingIntraBalance <UndrlygIntraBal>
Presence: [0..1]
Definition: Intra-balance movement transaction details.
Impacted by: C3 "AdditionalDetailsRule", C5 "BalanceFromToRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 206 August 2026
```

## File page 207

```text
UnderlyingIntraBalance <UndrlygIntraBal> contains the following IntraBalance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 208
   SettlementDate <SttlmDt> [1..1] ± 208
   BalanceFrom <BalFr> [1..1]  208
     Type <Tp> [1..1]  208
{Or       Code <Cd> [1..1] CodeSet 209
Or}       Proprietary <Prtry> [1..1] ± 209
     QuantityBreakdown <QtyBrkdwn> [0..*]  209
       LotNumber <LotNb> [0..1] ± 209
       LotAmount <LotAmt> [0..1] ± 210
       LotQuantity <LotQty> [0..1] ± 210
       CashSubBalanceType <CshSubBalTp> [0..1] ± 210
   BalanceTo <BalTo> [1..1]  211
     Type <Tp> [1..1]  211
{Or       Code <Cd> [1..1] CodeSet 211
Or}       Proprietary <Prtry> [1..1] ± 211
     QuantityBreakdown <QtyBrkdwn> [0..*]  212
       LotNumber <LotNb> [0..1] ± 212
       LotAmount <LotAmt> [0..1] ± 212
       LotQuantity <LotQty> [0..1] ± 213
       CashSubBalanceType <CshSubBalTp> [0..1] ± 213
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 213
   Priority <Prty> [0..1] ± 213
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 214
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
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 207 August 2026
```

