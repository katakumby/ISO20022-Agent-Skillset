---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.4 CancelledStatusReason16Code"]
file_pages: [474]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.4 CancelledStatusReason16Code

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 474 to 474.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 474

```text
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
12.2.2.4  CancelledStatusReason16Code
Definition: Specifies the reason for the cancellation status.
Type: CodeSet
Format
minLength 1
maxLength 4
CodeName Name Definition
SCEX SecuritiesNoLongerEligible Transaction has been cancelled; the
security no longer exists or is no longer
eligible on the market instructed. For
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
BYIY CancelledDueToBuyIn Instruction has been cancelled because
a buy-in has been initiated.
CTHP CancelledByThirdParty Instruction is cancelled by a Third party.
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CANS CancelledBySystem Transaction is cancelled by the system.
CANI CancelledByYourself Transaction is cancelled by yourself.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 474
```

