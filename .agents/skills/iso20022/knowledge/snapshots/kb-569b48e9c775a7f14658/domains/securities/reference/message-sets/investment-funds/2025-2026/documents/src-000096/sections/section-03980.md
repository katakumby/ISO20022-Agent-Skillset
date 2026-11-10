---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.25 BusinessFlowType1Code"]
file_pages: [5279]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.25 BusinessFlowType1Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5279 to 5279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5279

```text
66.2.2.25  BusinessFlowType1Code
Definition: Identifies the business process in which the actors are involved. This is important to trigger
the right business process, according to the market business model, which may require matching
instructions in a CSD environment (double leg process) or not (single leg process).
Type: CodeSet
CodeName Name Definition
SLDP SingleLegDeliveringParty Single leg process initiated by the
delivering party.
SLRP SingleLegReceivingParty Single leg process initiated by the
receiving party.
DLPR DoubleLegProcess Double leg process.
66.2.2.26  CalculationBasis2Code
Definition: Specifies the calculation basis.
Type: CodeSet
CodeName Name Definition
AVER Average Average basis.
DAIL Daily Daily basis.
MNTH Monthly Monthly basis.
YEAR Annual Yearly basis.
66.2.2.27  CancellationRejectedReason1Code
Definition: Specifies the reason for a cancellation rejected status.
Type: CodeSet
CodeName Name Definition
CUTO CutOffTime Instruction has been received after the
cut-off time.
COSE AlreadyExecuted Order or transfer has already been
executed and confirmation has been
sent.
66.2.2.28  CancellationRight1Code
Definition: Specifies if the investor has the right to cancel an instruction or, if not, the reason the investor
cannot cancel.
Type: CodeSet
CodeName Name Definition
VALI Entitled Investor is entitled to a "cooling off"
period with cancellation rights under
compliance rules.
NOXO ExecutionOnly Investor is not entitled to cancellation
rights under compliance rules, as the
investor is an execution's only client.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5279 May 2026
```

