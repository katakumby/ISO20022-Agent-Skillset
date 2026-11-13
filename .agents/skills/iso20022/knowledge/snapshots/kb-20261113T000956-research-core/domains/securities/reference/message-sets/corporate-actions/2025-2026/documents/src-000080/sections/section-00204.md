---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09", "4.4 Message Building Blocks", "4.4.4 EventProcessingStatus <EvtPrcgSts>", "4.4.4.1 Complete <Cmplt>"]
file_pages: [271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.032.001.09"]
---

# 4.4.4.1 Complete <Cmplt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 271 to 271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 271

```text
Definition: Information about the status of the corporate action.
EventProcessingStatus <EvtPrcgSts> contains one of the following
EventProcessingStatus7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Complete <Cmplt> [1..1] ± 271
Or   Reconciled <Rcncld> [1..1] ± 271
Or   Pending <Pdg> [1..1] ± 271
Or}   ProprietaryStatus <PrtrySts> [1..1] ± 272
4.4.4.1  Complete <Cmplt>
Presence: [1..1]
Definition: Specifies that a corporate action event processing has been completed.
Complete <Cmplt> contains the following elements (see "NoSpecifiedReason1" on page 1144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
4.4.4.2  Reconciled <Rcncld>
Presence: [1..1]
Definition: Corporate action event processing specifying that the funds paid have been reconciled with
the funds received from the agent (meaning that there is no more risk of payment to be reversed).
Reconciled <Rcncld> contains the following elements (see "NoSpecifiedReason1" on page 1144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
4.4.4.3  Pending <Pdg>
Presence: [1..1]
Definition: Specifies that a corporate action event processing has not been fully completed and is
therefore pending.
Pending <Pdg> contains one of the following elements (see "PendingStatus74Choice" on page 988 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 988
Or}   Reason <Rsn> [1..*] ± C1 988
Approved by the Securities SEG on 27 January 2026 seev.032.001.09
CorporateActionEventProcessingStatusAdviceV09
Corporate Actions - Maintenance 2025 - 2026 271 February 2026
```

