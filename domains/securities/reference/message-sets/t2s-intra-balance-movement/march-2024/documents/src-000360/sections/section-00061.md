---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "5.4 Message Building Blocks", "5.4.4 CashAccountServicer <CshAcctSvcr>"]
file_pages: [74, 75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 5.4.4 CashAccountServicer <CshAcctSvcr>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 74 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 420
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 420
5.4.4 CashAccountServicer <CshAcctSvcr>
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
5.4.5 RequestDetails <ReqDtls>
Presence: [1..*]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C12 "ModificationRequestPresenceRule", C13 "OtherProcessingRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
74 March 2024
```

## File page 75

```text
RequestDetails <ReqDtls> contains the following RequestDetails22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  76
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 76
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 76
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 76
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 76
     PoolIdentification <PoolId> [0..1] Text 77
   Linkage <Lkg> [0..1] ± 77
   Priority <Prty> [0..1] ± 77
   OtherProcessing <OthrPrcg> [0..*] ± 77
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 77
   ClearingChannel <ClrChanl> [0..1] CodeSet 78
   Linkages <Lnkgs> [0..*]  78
     ProcessingPosition <PrcgPos> [0..1] ± C16 79
     MessageNumber <MsgNb> [0..1] ± C14 79
     Reference <Ref> [1..1]  79
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 80
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 80
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 80
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 80
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 80
Or       PoolIdentification <PoolId> [1..1] Text 81
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 81
     ReferenceOwner <RefOwnr> [0..1] ± 81
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
75 March 2024
```

