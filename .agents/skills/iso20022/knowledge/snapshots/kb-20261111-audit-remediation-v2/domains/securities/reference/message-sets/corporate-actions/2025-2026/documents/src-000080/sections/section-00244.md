---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.2 Structure"]
file_pages: [322, 323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.2 Structure

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 322 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 322

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnInstrStsAdvc> [1..1]  C2, C10,
C29,
C30,
C31,
C32,
C33,
C34,
C35,
C36,
C37
   InstructionIdentification <InstrId> [0..1] ± 330
   OtherDocumentIdentification <OthrDocId> [0..*] ± 330
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C16,
C21
331
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 332
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 332
     ClassActionNumber <ClssActnNb> [0..1] Text 332
     BuyerProtectionInstructionIdentification <BuyrPrtcnInstrId> [0..1] Text 332
     EventType <EvtTp> [1..1] ± C17 332
   InstructionProcessingStatus <InstrPrcgSts> [1..*]  333
{Or     Cancelled <Canc> [1..1] ± 335
Or     AcceptedForFurtherProcessing <AccptdForFrthrPrcg> [1..1] ± 335
Or     Forwarded <Fwdd> [1..1]  335
       ForwardedQuantity <FwddQty> [0..1] ± 336
       ForwardedReason <FwddRsn> [1..1] ± 336
Or     Rejected <Rjctd> [1..1]  336
       RejectedQuantity <RjctdQty> [0..1] ± 337
       RejectedReason <RjctdRsn> [1..1]  337
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 337
Or}         Reason <Rsn> [1..*]  C5 338
           ReasonCode <RsnCd> [1..1]  338
{Or             Code <Cd> [1..1] CodeSet 338
Or}             Proprietary <Prtry> [1..1] ± 341
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 341
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 322 February 2026
```

## File page 323

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or     Pending <Pdg> [1..1]  341
       PendingQuantity <PdgQty> [0..1] ± 341
       PendingReason <PdgRsn> [1..1]  342
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 342
Or}         Reason <Rsn> [1..*]  C6 342
           ReasonCode <RsnCd> [1..1]  343
{Or             Code <Cd> [1..1] CodeSet 343
Or}             Proprietary <Prtry> [1..1] ± 344
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 344
Or     Returned <Rtrd> [1..1]  345
       ReturnedQuantity <RtrdQty> [0..1] ± 345
       ReturnedReason <RtrdRsn> [1..1]  345
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 346
Or}         Reason <Rsn> [1..*]  C7 346
           ReasonCode <RsnCd> [1..1]  346
{Or             Code <Cd> [1..1] CodeSet 347
Or}             Proprietary <Prtry> [1..1] ± 347
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 347
Or     DefaultAction <DfltActn> [1..1] ± 347
Or     StandingInstruction <StgInstr> [1..1] ± 348
Or     ReceivedByIssuerOrOfferor <RcvdByIssrOrOfferr> [1..1]  348
       AcceptedByIssuerQuantity <AccptdByIssrQty> [0..1] ± 348
       ReceivedByIssuerOrOfferorReason
<RcvdByIssrOrOfferrRsn>
[1..1] ± 348
Or}     ProprietaryStatus <PrtrySts> [1..1] ± 348
   CorporateActionInstruction <CorpActnInstr> [0..1]  C22,
C24,
C25,
C26,
C27
349
     OptionNumber <OptnNb> [1..1] ± 350
     OptionType <OptnTp> [1..1] ± 350
     OptionFeatures <OptnFeatrs> [0..1] ± 351
     AccountOwner <AcctOwnr> [0..1] ± 351
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 323 February 2026
```

