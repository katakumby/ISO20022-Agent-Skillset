---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.4 AdditionalBusinessProcess10Code"]
file_pages: [1158]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.4 AdditionalBusinessProcess10Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1158 to 1158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1158

```text
Type: CodeSet
Format
pattern [A-Z]{3,3}
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
16.2.2.4  AdditionalBusinessProcess10Code
Definition: Specifies the additional business process linked to a corporate action event.
Type: CodeSet
CodeName Name Definition
CLAI ClaimOrCompensation Relates to a claim on the associated
corporate action event.
REVR NotificationOfReversal Indicates a preadvice of movement
reversal.
TAXR TaxRefund Relates to a tax refund from the
authorities on the associated corporate
action event.
PPUT PartialMandatoryPutRedemption Partial mandatory exchange of a portion
of bonds where the exchanged securities
are usually remarketed. The issuer may
offer holders the right to retain instead of
exchanging their securities. A lottery will
be used to determine eligibility for the
event.
PPRE PartialPreFunding Partial pre-funding of a debt instrument
prior to maturity drawn through a lottery
process. One new security is issued with
an earlier maturity date for the refunded
(called portion) and the other new
security is issued with the original
maturity date for the non refunded
(remaining) portion. Applicable only in
the frame of a partial defeasance
corporate action event.
FPRE FullPrefunding Full pre-funding of a debt instrument by
the issuer prior to original maturity when
the issuer deposits assets in trust.
Applicable only in the frame of a partial
defeasance corporate action event.
REAC RequiredAction Proceeds / entitlements of the
mandatory event can only be paid if
specified action is taken by the account
owner.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1158 February 2026
```

