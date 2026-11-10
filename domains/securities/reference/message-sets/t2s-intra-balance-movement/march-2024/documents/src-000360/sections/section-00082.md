---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "6.4 Message Building Blocks", "6.4.6 RequestDetails <ReqDtls>"]
file_pages: [99, 100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 6.4.6 RequestDetails <ReqDtls>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 99 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

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
6.4.6 RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C13 "ModificationRequestPresenceRule", C14 "OtherProcessingRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
99 March 2024
```

## File page 100

```text
RequestDetails <ReqDtls> contains the following RequestDetails22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  101
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 101
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 101
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 101
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 101
     PoolIdentification <PoolId> [0..1] Text 102
   Linkage <Lkg> [0..1] ± 102
   Priority <Prty> [0..1] ± 102
   OtherProcessing <OthrPrcg> [0..*] ± 102
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 102
   ClearingChannel <ClrChanl> [0..1] CodeSet 103
   Linkages <Lnkgs> [0..*]  103
     ProcessingPosition <PrcgPos> [0..1] ± C17 104
     MessageNumber <MsgNb> [0..1] ± C15 104
     Reference <Ref> [1..1]  104
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 105
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 105
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 105
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 105
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 105
Or       PoolIdentification <PoolId> [1..1] Text 106
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 106
     ReferenceOwner <RefOwnr> [0..1] ± 106
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
100 March 2024
```

