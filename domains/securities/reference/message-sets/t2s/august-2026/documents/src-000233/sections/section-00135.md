---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.4 Message Building Blocks", "11.4.6 RequestDetails <ReqDtls>"]
file_pages: [182, 183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.4.6 RequestDetails <ReqDtls>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 182 to 183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 182

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
11.4.6 RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request providing the changes and references of the instruction for which the
modification is requested.
Impacted by: C13 "ModificationRequestPresenceRule", C14 "OtherProcessingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 182 August 2026
```

## File page 183

```text
RequestDetails <ReqDtls> contains the following RequestDetails22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1]  184
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 184
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 184
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 184
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 184
     PoolIdentification <PoolId> [0..1] Text 185
   Linkage <Lkg> [0..1] ± 185
   Priority <Prty> [0..1] ± 185
   OtherProcessing <OthrPrcg> [0..*] ± 185
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 185
   ClearingChannel <ClrChanl> [0..1] CodeSet 186
   Linkages <Lnkgs> [0..*]  186
     ProcessingPosition <PrcgPos> [0..1] ± C17 187
     MessageNumber <MsgNb> [0..1] ± C15 187
     Reference <Ref> [1..1]  187
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 188
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 188
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 188
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 188
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 188
Or       PoolIdentification <PoolId> [1..1] Text 189
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 189
     ReferenceOwner <RefOwnr> [0..1] ± 189
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 183 August 2026
```

