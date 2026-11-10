---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.4 Message Building Blocks", "10.4.4 CashAccountServicer <CshAcctSvcr>"]
file_pages: [157, 158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.4.4 CashAccountServicer <CshAcctSvcr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 157 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 157

```text
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
10.4.4 CashAccountServicer <CshAcctSvcr>
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
10.4.5 RequestDetails <ReqDtls>
Presence: [1..*]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C12 "ModificationRequestPresenceRule", C13 "OtherProcessingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 157 August 2026
```

## File page 158

```text
RequestDetails <ReqDtls> contains the following RequestDetails22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  159
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 159
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 159
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 159
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
     PoolIdentification <PoolId> [0..1] Text 160
   Linkage <Lkg> [0..1] ± 160
   Priority <Prty> [0..1] ± 160
   OtherProcessing <OthrPrcg> [0..*] ± 160
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 160
   ClearingChannel <ClrChanl> [0..1] CodeSet 161
   Linkages <Lnkgs> [0..*]  161
     ProcessingPosition <PrcgPos> [0..1] ± C16 162
     MessageNumber <MsgNb> [0..1] ± C14 162
     Reference <Ref> [1..1]  162
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 163
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 163
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 163
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 163
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 163
Or       PoolIdentification <PoolId> [1..1] Text 164
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 164
     ReferenceOwner <RefOwnr> [0..1] ± 164
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 158 August 2026
```

