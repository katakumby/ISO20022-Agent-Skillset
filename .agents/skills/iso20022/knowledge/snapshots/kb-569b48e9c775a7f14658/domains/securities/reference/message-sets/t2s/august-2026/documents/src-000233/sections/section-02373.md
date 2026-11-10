---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.24 AcknowledgementReason12Choice", "82.1.30.24.2 Proprietary <Prtry>"]
file_pages: [3160]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.24.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3160 to 3160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3160

```text
CodeName Name Definition
OTHR Other Other. See Narrative.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
NSTP NotStraightThroughProcessing Instruction was not straight through
processing and had to be processed
manually.
RQWV AcceptedWithoutVotingRights Instruction registration is accepted but
the registration is not in full, that is, not
with voting rights.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
82.1.30.24.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.25  DeniedStatus16Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3160
Or}   Reason <Rsn> [1..*]  3161
     Code <Cd> [1..1] ± 3161
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3161
82.1.30.25.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3160 August 2026
```

