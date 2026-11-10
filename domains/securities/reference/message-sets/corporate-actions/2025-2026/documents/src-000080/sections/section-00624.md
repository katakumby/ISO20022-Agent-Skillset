---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.2 Structure"]
file_pages: [815]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 815 to 815.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 815

```text
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnMvmntPrlimryAdvcCxlAdvc> [1..1]  
   MovementPreliminaryAdviceIdentification
<MvmntPrlimryAdvcId>
[1..1] ± 817
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C8 818
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 818
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 818
     ClassActionNumber <ClssActnNb> [0..1] Text 818
     EventType <EvtTp> [1..1] ± C5 819
     MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 819
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C6, C7,
C9
819
   AccountDetails <AcctDtls> [1..1]  820
{Or     ForAllAccounts <ForAllAccts> [1..1] ± 821
Or}     AccountsList <AcctsList> [1..*]  C10,
C11,
C12,
C13
821
       SafekeepingAccount <SfkpgAcct> [0..1] Text 822
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 822
       AccountOwner <AcctOwnr> [0..1] ± 822
       SafekeepingPlace <SfkpgPlc> [0..1] ± 822
   CorporateActionDetails <CorpActnDtls> [0..1]  823
     DateDetails <DtDtls> [0..1]  823
       RecordDate <RcrdDt> [0..1] ± 823
       ExDividendDate <ExDvddDt> [0..1] ± 824
     EventStage <EvtStag> [0..1] ± 824
     LotteryType <LtryTp> [0..1] ± 824
   IssuerAgent <IssrAgt> [0..*] ± 825
   PayingAgent <PngAgt> [0..*] ± 825
   SubPayingAgent <SubPngAgt> [0..*] ± 825
   Registrar <Regar> [0..1] ± 826
   ResellingAgent <RsellngAgt> [0..*] ± 826
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 815 February 2026
```

