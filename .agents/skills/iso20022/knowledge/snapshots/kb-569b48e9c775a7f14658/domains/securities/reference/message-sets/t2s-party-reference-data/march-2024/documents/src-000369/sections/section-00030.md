---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 reda.016.001.01 PartyStatusAdviceV01", "4.2 Structure"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 4.2 Structure

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  37
     MessageIdentification <MsgId> [1..1] Text 37
     CreationDateTime <CreDtTm> [0..1] DateTime 37
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 37
   PartyStatus <PtySts> [1..1]  C3, C4 37
     Status <Sts> [1..1] CodeSet 38
     StatusReason <StsRsn> [0..*]  38
       Reason <Rsn> [1..1]  39
{Or         Code <Cd> [1..1] CodeSet 39
Or}         Proprietary <Prtry> [1..1] Text 39
       AdditionalInformation <AddtlInf> [0..1] Text 39
     SystemPartyIdentification <SysPtyId> [0..1] ± 39
   SupplementaryData <SplmtryData> [0..*] ± C5 40
4.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 PartyPresenceRule
If Status equals 'Completed' then RelatedPartyIdentification must be present and
ResponsiblePartyIdentification must be present.
C4 StatusReasonRule
If Status equals 'Rejected' then StatusReason must be present.
C5 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
36 March 2024
```

