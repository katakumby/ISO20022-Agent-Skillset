---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["2 camt.064.001.01 LimitUtilisationJournalQueryV01"]
file_pages: [4]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.064.001.01"]
---

# 2 camt.064.001.01 LimitUtilisationJournalQueryV01

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 4 to 4.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
2 camt.064.001.01
LimitUtilisationJournalQueryV01
2.1 MessageDefinition Functionality
The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a
directly connected system participant (the central securities depository participant granted direct
access, like a bank or a central counter party) and the central system. Its purpose is to query
information regarding the journal of transaction impacting the utilisation of limits that have been defined
by the system participant.
Outline
The LimitUtilisationJournalQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements used to provide information on the header of the message.
B. SearchCriteria
Provides criteria in the form of business attributes to define result set.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <LmtUtlstnJrnlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 5
   SearchCriteria <SchCrit> [1..1]  5
     LimitType <LmtTp> [0..*] CodeSet 6
     JournalActivityDate <JrnlActvtyDt> [1..1] Date 6
     AccountIdentification <AcctId> [0..1] ± 6
     LimitCurrency <LmtCcy> [0..1] CodeSet C1 7
     AccountOwner <AcctOwnr> [0..1] ± 7
     BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [1..1] ± 7
   SupplementaryData <SplmtryData> [0..*] ± C5 8
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.064.001.01 LimitUtilisationJournalQueryV01
Target2-Securities - Limit Utilisation Journal 4 February 2025
```

