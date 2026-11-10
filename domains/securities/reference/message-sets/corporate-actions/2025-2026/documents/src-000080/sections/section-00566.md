---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.2 Structure"]
file_pages: [735]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 735 to 735.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 735

```text
13.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnInstrCxlReqStsAdvc> [1..1]  C2, C8
   InstructionCancellationRequestIdentification <InstrCxlReqId> [0..1] ± 739
   OtherDocumentIdentification <OthrDocId> [0..*] ± 739
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C14,
C19
740
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 741
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 741
     ClassActionNumber <ClssActnNb> [0..1] Text 741
     EventType <EvtTp> [1..1] ± C15 741
   InstructionCancellationRequestStatus <InstrCxlReqSts> [1..*]  742
{Or     CancellationCompleted <CxlCmpltd> [1..1] ± 742
Or     Accepted <Accptd> [1..1] ± 743
Or     Rejected <Rjctd> [1..1]  743
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 743
Or}       Reason <Rsn> [1..*]  C4 743
         ReasonCode <RsnCd> [1..1]  744
{Or           Code <Cd> [1..1] CodeSet 744
Or}           Proprietary <Prtry> [1..1] ± 745
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 745
Or     PendingCancellation <PdgCxl> [1..1] ± 745
Or}     ProprietaryStatus <PrtrySts> [1..1] ± 746
   CorporateActionInstruction <CorpActnInstr> [0..1]  C20,
C22,
C23,
C24,
C25,
C27,
C28
746
     OptionNumber <OptnNb> [1..1] ± 748
     OptionType <OptnTp> [1..1] ± 748
     OptionFeatures <OptnFeatrs> [0..1] ± 748
     AccountOwner <AcctOwnr> [0..1] ± 749
     SafekeepingAccount <SfkpgAcct> [0..1] Text 749
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 735 February 2026
```

