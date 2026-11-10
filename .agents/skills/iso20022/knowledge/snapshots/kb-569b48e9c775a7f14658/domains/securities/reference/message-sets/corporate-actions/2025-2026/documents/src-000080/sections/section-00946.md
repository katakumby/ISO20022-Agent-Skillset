---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.15 BidRangeType1Code"]
file_pages: [1165]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.15 BidRangeType1Code

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1165 to 1165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1165

```text
CodeName Name Definition
option level can be offered at the
beneficial owner level.
PAPW BeneficialOwnerPaperwork Indicates if the Beneficial Owner is
responsible to fill in the paperwork.
DIOR IntermediaryDocumentationRequired Documentation required on or prior to
the documentation deadline date.
16.2.2.15  BidRangeType1Code
Definition: Types of acceptable bid range values.
Type: CodeSet
CodeName Name Definition
DIVI Divisible All values (including minimum and
maximum prices) are divisible by the bid
interval.
INCR Incremental No values within the bid range are
divisible by the bid interval including the
minimum and maximum prices. Each
value between the minimum and
maximum prices is incremented by the
bid interval.
MULT InMultiple Minimum and maximum prices are not
divisible by the bid interval. All
successive values between the minimum
and maximum prices are in multiples of
the bid interval.
16.2.2.16  BusinessMessagePriorityCode
Definition: Specifies the priority levels for the BusinessMessage.
The different priorities are typically user / service / implementation dependent. The semantics of the
different values for a Mesage (Set) need to be defined by the relevant user community (SEG.).
Type: CodeSet
Constraints
• ValidationByTable
16.2.2.17  CancelledStatusReason5Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
OTHR Other Other. See Narrative.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1165 February 2026
```

