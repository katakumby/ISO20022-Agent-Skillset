---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.11 MatchingStatus24Choice", "7.1.28.11.2 Unmatched <Umtchd>", "7.1.28.11.2.2 Reason <Rsn>", "7.1.28.11.2.2.1 Code <Cd>", "7.1.28.11.2.2.1.2 Proprietary <Prtry>"]
file_pages: [481]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.11.2.2.1.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 481 to 481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 481

```text
7.1.28.11.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.28.11.2.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 556
7.1.28.11.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 469
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 469
   ProprietaryReason <PrtryRsn> [0..*] ± C6 469
7.1.28.12  AcknowledgedAcceptedStatus21Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 481
Or}   Reason <Rsn> [1..*] ± 482
7.1.28.12.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 481 March 2026
```

