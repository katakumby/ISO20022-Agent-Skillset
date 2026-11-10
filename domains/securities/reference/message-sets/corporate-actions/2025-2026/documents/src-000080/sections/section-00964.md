---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.52 DateType8Code"]
file_pages: [1206]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.52 DateType8Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1206 to 1206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1206

```text
16.2.2.52  DateType8Code
Definition: Specifies the type of dates.
Type: CodeSet
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.2.2.53  DateType9Code
Definition: Date is specified as a fixed code value.
Type: CodeSet
CodeName Name Definition
PWAL BlockingTillEndOfElectionPeriod Blocking occurs until and inclusive of the
end of the election period of the option.
MKDT BlockingTillMarketDeadline Blocking occurs until and inclusive of the
market deadline of the option.
MEET BlockingTillMeetingDate Blocking occurs until and inclusive of the
meeting date.
PAYD BlockingTillPaymentDate Unblocking will occur on payment date of
the option.
RDTE BlockingTillRecordDate Blocking occurs until and inclusive of the
record date of the event.
RDDT BlockingTillResponseDeadline Blocking occurs until and inclusive of the
account servicer deadline for the option.
NARR NarrativeUnblockingDate Refer to additional information element
for the date until when the securities are
blocked.
UKWN Unknown Date is unknown by the sender or has
not been established.
16.2.2.54  DeemedRateType1Code
Definition: Specifies the type of a deemed rate.
Type: CodeSet
CodeName Name Definition
DEDI DeemedDividendProceeds Deemed rate of dividend proceeds
attributed to the security holder.
DEFP DeemedFundProceeds Deemed rate of fund proceeds attributed
to the security holder.
DEIT DeemedInterestProceeds Deemed rate of interest proceeds
attributed to the security holder.
DERY DeemedRoyaltiesProceeds Deemed rate of royalties proceeds
attributed to the security holder.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1206 February 2026
```

