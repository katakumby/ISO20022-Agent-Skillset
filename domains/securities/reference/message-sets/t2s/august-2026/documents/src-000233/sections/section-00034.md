---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["5 camt.064.001.01 LimitUtilisationJournalQueryV01"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.064.001.01"]
---

# 5 camt.064.001.01 LimitUtilisationJournalQueryV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
5 camt.064.001.01
LimitUtilisationJournalQueryV01
5.1 MessageDefinition Functionality
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
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <LmtUtlstnJrnlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 69
   SearchCriteria <SchCrit> [1..1]  69
     LimitType <LmtTp> [0..*] CodeSet 70
     JournalActivityDate <JrnlActvtyDt> [1..1] Date 70
     AccountIdentification <AcctId> [0..1] ± 70
     LimitCurrency <LmtCcy> [0..1] CodeSet C1 71
     AccountOwner <AcctOwnr> [0..1] ± 71
     BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [1..1] ± 71
   SupplementaryData <SplmtryData> [0..*] ± C5 72
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.064.001.01 LimitUtilisationJournalQueryV01
Target2-Securities 68 August 2026
```

