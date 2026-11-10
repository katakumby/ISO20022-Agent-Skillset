---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.2 Structure"]
file_pages: [703]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 703 to 703.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 703

```text
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnCxlAdvc> [1..1]  
   CancellationAdviceGeneralInformation <CxlAdvcGnlInf> [1..1]  705
     CancellationReasonCode <CxlRsnCd> [1..1] CodeSet 706
     CancellationReason <CxlRsn> [0..1] Text 706
     ProcessingStatus <PrcgSts> [1..1]  706
       EventCompletenessStatus <EvtCmpltnsSts> [1..1] CodeSet 706
       EventConfirmationStatus <EvtConfSts> [1..1] CodeSet 707
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C8 707
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 708
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 708
     ClassActionNumber <ClssActnNb> [0..1] Text 708
     EventType <EvtTp> [1..1] ± C5 708
     MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 709
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C6, C7,
C9
709
   AccountsDetails <AcctsDtls> [1..1]  710
{Or     ForAllAccounts <ForAllAccts> [1..1] ± 710
Or}     AccountsList <AcctsList> [1..*]  C10,
C11,
C12,
C13
711
       SafekeepingAccount <SfkpgAcct> [0..1] Text 711
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 712
       AccountOwner <AcctOwnr> [0..1] ± 712
       SafekeepingPlace <SfkpgPlc> [0..1] ± 712
   CorporateActionDetails <CorpActnDtls> [0..1]  712
     DateDetails <DtDtls> [0..1]  713
       RecordDate <RcrdDt> [0..1] ± 713
       ExDividendDate <ExDvddDt> [0..1] ± 713
     EventStage <EvtStag> [0..1] ± 714
     AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 714
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 703 February 2026
```

