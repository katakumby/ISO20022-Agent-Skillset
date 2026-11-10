---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["36 reda.016.001.01 PartyStatusAdviceV01", "36.2 Structure"]
file_pages: [2073]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 36.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2073 to 2073.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2073

```text
36.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2074
     MessageIdentification <MsgId> [1..1] Text 2074
     CreationDateTime <CreDtTm> [0..1] DateTime 2074
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2074
   PartyStatus <PtySts> [1..1]  C3, C4 2074
     Status <Sts> [1..1] CodeSet 2075
     StatusReason <StsRsn> [0..*]  2075
       Reason <Rsn> [1..1]  2076
{Or         Code <Cd> [1..1] CodeSet 2076
Or}         Proprietary <Prtry> [1..1] Text 2076
       AdditionalInformation <AddtlInf> [0..1] Text 2076
     SystemPartyIdentification <SysPtyId> [0..1] ± 2076
   SupplementaryData <SplmtryData> [0..*] ± C5 2077
36.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities 2073 August 2026
```

