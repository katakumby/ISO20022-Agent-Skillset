---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Background"]
content_origin: "source-transcription"
---

# Background

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Scope and Functionality / Background.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P122** Background

**P123** This Message Definition Report describes a set of 33 ISO 20022 MessageDefinitions developed by SWIFT in close collaboration with the ISO 15022/ISO 20022 community of users. Most of these ISO 20022 message definitions were reverse engineered from ISO 15022 messages. 

**P124** These messages are specifically designed to support the settlement and reconciliation business processes.

**P125** The ISO 15022 and ISO 20022 standards will coexist for a number of years. Until this coexistence period ends, SWIFT will maintain a set of "ISO 15022 variants" of the Settlement and Reconciliation MessageDefinitions, where certain data types are restricted to ensure full interoperability between ISO 15022 and ISO 20022 users. These restrictions have been implemented directly in the message schema of the variants. 

**P126** This set of messages will be used by intermediaries involved in the settlement and reconciliation processing chain, for example, brokers, investment managers, global custodians, stock exchanges and market infrastructures.

**P127** Historical background

**P128** With harmonisation industry initiatives such as Giovannini (an EU harmonisation workgroup that was conducted about 10 years ago which identified barriers in post trade services), there is an increasing pressure on the securities industry to go from proprietary standards to ISO standards.

**P129** SWIFT was requested by its community to develop ISO 20022 messages equivalent to ISO 15022 to allow ISO 'newcomers' to directly adopt ISO 20022. To limit the impact on existing ISO 15022 users, the ISO 20022 messages were directly reversed engineered from ISO 15022 messages. 

**P130** In this process, SWIFT made sure to:

**P131** design the ISO 20022 messages with mapping to ISO 15022 in mind to ensure the same levels of STP as today,

**P132** limit the ISO 20022 functionality to the functionality available in ISO 15022 during the coexistence period. That is, it would not be possible to do something with an ISO 20022 message that could not be done in its equivalent ISO 15022 messages and vice versa,

**P133** synchronise the maintenance between the two standards in terms of timing, review process and content,

**P134** provide coexistence support, for example, the necessary mapping or translation documentation.

**P135** In addition to the above, SWIFT undertook the following tasks to ensure that the right balance was kept between the need for close reverse engineering from ISO 15022 and the need for leveraging the benefits and principles of ISO 20022:

**P136** ensure that global market practices defined by the Securities Market Practice Group (SMPG) were adhered to during the process,

**P137** solve ISO 15022 standards issues that were identified by the ISO 15022 Registration Authority and the SMPG and that had been postponed awaiting equivalent ISO 20022 messages,

**P138** ensure that additional requirements identified by harmonisation initiatives such as Giovannini were included, in both ISO 15022 and ISO 20022 unless agreed otherwise,

**P139** design the financial instruments identification and attributes based upon the Financial Instrument Business Information Model (FIBIM) as defined by ISO TC 68 SC 4 WG 11. 

**P140** 	

